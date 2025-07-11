# Guia de Licenças Open Source

Escolher uma licença é um passo fundamental em qualquer projeto open source. Ela define o que outras pessoas podem (e não podem) fazer com seu código.

Abaixo estão as licenças mais populares, divididas em duas categorias principais: **Permissivas** e **Copyleft**.

---

## 1. Licenças Permissivas

Essas licenças dão liberdade máxima para quem usa o código. Elas têm poucas restrições sobre como o software pode ser usado, modificado e redistribuído.

### MIT License

* **Resumo:** "Faça o que quiser com meu código, desde que você mantenha meu aviso de copyright e o texto da licença."
* **Na prática:** É a licença mais popular e simples. Permite o uso em projetos comerciais e de código fechado (proprietários) sem problemas. É ideal para quem quer que seu código seja usado pelo maior número de pessoas possível, sem se preocupar com o que farão com ele.

### Apache License 2.0

* **Resumo:** "Faça o que quiser, mas se você modificar o código, precisa indicar as mudanças. Além disso, eu te concedo o direito de usar minhas patentes, e você me concede o direito de usar as suas se contribuir."
* **Na prática:** É muito parecida com a MIT, mas mais detalhada e com uma cláusula explícita sobre direitos de patente. É uma escolha corporativa muito comum, pois oferece mais segurança jurídica.

### BSD License (3-Clause)

* **Resumo:** "Faça o que quiser, mas não use meu nome para promover seu produto sem permissão."
* **Na prática:** É funcionalmente muito similar à licença MIT. A principal diferença é a cláusula que proíbe o uso do nome dos autores originais para endossar um produto derivado.

---

## 2. Licenças Copyleft

O conceito de "Copyleft" (um trocadilho com "Copyright") significa que qualquer software derivado do código original também deve ser distribuído sob os mesmos termos. O objetivo é garantir que o software permaneça livre para sempre.

### GNU General Public License (GPLv3)

* **Resumo:** "Você pode usar, modificar e distribuir meu código, mas se você criar um programa derivado e distribuí-lo, seu programa também **deve** ser licenciado sob a GPLv3."
* **Na prática:** É uma licença "viral". Se você usar um componente GPL no seu projeto, seu projeto inteiro (se distribuído) também precisa ser GPL. Ela é ideal para garantir que as contribuições à comunidade permaneçam na comunidade. É a licença do Linux, por exemplo.

### Mozilla Public License 2.0 (MPL 2.0)

* **Resumo:** "Você pode usar meu código em seu projeto maior (mesmo que seja proprietário). Se você modificar meus arquivos, você deve compartilhar as modificações desses arquivos específicos. O resto do seu projeto pode ter outra licença."
* **Na prática:** É um meio-termo. É considerada uma licença "copyleft fraca" ou "por arquivo". Ela garante que as melhorias no código original voltem para a comunidade, mas sem "infectar" o resto do projeto. É a licença do Firefox.
