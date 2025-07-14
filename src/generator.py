import shutil
import os
from pathlib import Path

# --- Configuração ---
# Define caminhos com base na localização do script para robustez
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent

# Arquivos de origem estão em 'src' ou no root do projeto
IMG_DIR = PROJECT_ROOT / 'images'
TEMPLATE_FILE = SCRIPT_DIR / 'template.html'
CSS_FILE = SCRIPT_DIR / 'style.css'
FOLDER_ICON_FILE = SCRIPT_DIR / 'folder-icon.svg'  # Ícone para as pastas
FAVICON_FILE = SCRIPT_DIR / 'favicon.svg'          # Ícone para o navegador (favicon)

# O diretório de saída agora é 'pub' na raiz do projeto, uma prática mais segura
OUTPUT_DIR = PROJECT_ROOT / 'pub'

IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']

def generate_site():
    """Função principal que gera o site estático."""
    # 1. Garante que o diretório de saída 'pub' esteja limpo e exista.
    if OUTPUT_DIR.exists():
        # Limpa o conteúdo do diretório, mas não o diretório em si.
        # Isso é crucial para a execução com Docker, pois '/app/pub' é um ponto de montagem.
        for item in OUTPUT_DIR.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    else:
        # Se o diretório não existir (ex: primeira execução sem Docker), cria-o.
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Copia o arquivo CSS para a raiz do diretório de saída
    shutil.copy(CSS_FILE, OUTPUT_DIR / CSS_FILE.name)
    # Copia o ícone da pasta para a raiz do diretório de saída, se ele existir
    if FOLDER_ICON_FILE.exists():
        shutil.copy(FOLDER_ICON_FILE, OUTPUT_DIR / FOLDER_ICON_FILE.name)
    # Copia o favicon para a raiz do diretório de saída, se ele existir
    if FAVICON_FILE.exists():
        shutil.copy(FAVICON_FILE, OUTPUT_DIR / FAVICON_FILE.name)

    # 3. Lê o template HTML uma única vez
    template_html = TEMPLATE_FILE.read_text(encoding='utf-8')

    # 4. Percorre o diretório de imagens recursivamente
    # O primeiro item do walk é o próprio diretório raiz
    for root_str, dirs, files in sorted(os.walk(IMG_DIR)):
        root = Path(root_str)
        
        # Ordena diretórios e arquivos alfabeticamente para consistência
        dirs.sort()
        files.sort()

        # Calcula o caminho de saída para o HTML desta pasta
        relative_dir = root.relative_to(IMG_DIR)
        current_output_dir = OUTPUT_DIR / relative_dir
        current_output_dir.mkdir(exist_ok=True)
        output_html_path = current_output_dir / 'index.html'

        # --- Gera o conteúdo HTML (pastas e imagens) ---
        content_html = ''

        # Calcula o prefixo do caminho relativo para recursos na raiz (CSS, ícones)
        depth = len(relative_dir.parts) if relative_dir != Path('.') else 0
        path_prefix = ('../' * depth) if depth > 0 else './'

        # Adiciona subdiretórios
        for d in dirs:
            # O link aponta para o index.html dentro do subdiretório
            display_name = d.replace('_', ' ')
            icon_path = f"{path_prefix}{FOLDER_ICON_FILE.name}" if FOLDER_ICON_FILE.exists() else "https://via.placeholder.com/200x150.png/f0f0f0/333?text=Pasta"
            content_html += f'<div class="gallery-item folder"><a href="{d}/index.html"><img src="{icon_path}" alt="Ícone da pasta {display_name}"><div class="name">{display_name}</div></a></div>\n'
        # Adiciona imagens
        for f_name in files:
            file_path = Path(f_name)
            if file_path.suffix.lower() in IMAGE_EXTENSIONS:
                # Copia a imagem para o diretório de saída correspondente
                shutil.copy(root / file_path, current_output_dir / file_path.name)

                # Cria um nome de exibição mais legível para o atributo 'alt' e para o texto do item
                # Remove a extensão do arquivo e substitui underscores por espaços
                display_name = file_path.stem.replace('_', ' ')
                # O link no HTML é relativo ao próprio arquivo index.html
                content_html += f'<div class="gallery-item"><a href="{file_path.name}" target="_blank"><img src="{file_path.name}" alt="{display_name}"><div class="name">{display_name}</div></a></div>\n'

        # --- Gera os Breadcrumbs (caminho de navegação) ---
        # Lógica simplificada e mais robusta
        if relative_dir == Path('.'):
            breadcrumbs_html = '<a href="#">Início</a>'
            page_title = 'Galeria de Imagens'
        else:
            page_title = relative_dir.name
            depth = len(relative_dir.parts)
            # Link para a página inicial
            root_link = '/'.join(['..'] * depth) + '/index.html'
            breadcrumbs_html = f'<a href="{root_link}">Início</a>'
            # Links para as pastas intermediárias
            for i, part in enumerate(relative_dir.parts):
                levels_up = depth - (i + 1)
                link = '/'.join(['..'] * levels_up) + '/index.html' if levels_up > 0 else '#'
                breadcrumbs_html += f' / <a href="{link}">{part}</a>'

        # --- Monta a página final ---
        # Calcula o caminho relativo para o CSS a partir da página atual
        css_path = f"{path_prefix}{CSS_FILE.name}"
        favicon_path = f"{path_prefix}{FAVICON_FILE.name}"

        final_html = template_html.replace('{{title}}', page_title)
        final_html = final_html.replace('{{breadcrumbs}}', breadcrumbs_html)
        final_html = final_html.replace('{{content}}', content_html)
        final_html = final_html.replace('{{css_path}}', css_path)
        final_html = final_html.replace('{{favicon_path}}', favicon_path)

        # 5. Salva o arquivo HTML gerado
        output_html_path.write_text(final_html, encoding='utf-8')

        print(f"Gerado: {output_html_path}")

if __name__ == '__main__':
    if not IMG_DIR.is_dir():
        print(f"Erro: O diretório '{IMG_DIR}' não foi encontrado. Crie-o e adicione suas imagens.")
    elif not TEMPLATE_FILE.is_file() or not CSS_FILE.is_file():
        print(f"Erro: Verifique se os arquivos '{TEMPLATE_FILE}' e '{CSS_FILE}' existem no diretório 'src'.")
    else:
        generate_site()
        print(f"\nSite estático gerado com sucesso na pasta '{OUTPUT_DIR.name}'!")