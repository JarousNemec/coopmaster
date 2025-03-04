# CoopMaster
CoopMaster je chytrá aplikace pro správu kurníku, která automatizuje klíčové úkoly jako otevírání dveří a sledování zdraví slepic.
 Díky senzorům a kamerám zajišťuje bezpečnost a pohodlí slepic, zatímco farmář může kurník ovládat na dálku přes mobilní zařízení. Optimalizuje produkci a šetří čas díky automatizaci a monitoringu.

### Co je to Agilní vývoj
- https://thinkeasy.cz/co-je-agilni-vyvoj-a-proc-ho-pouzivame/

### Pravidla pojmenování pro python
- https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html

### Kontejneryzace a CI/CD

## Produktový Backlog
 - https://docs.google.com/document/d/1aPqurcaADt5CdIsI3ue-6VVS-13A8hmTuslFvSt8Ch0/edit?usp=sharing

## Sprintový backlog    
 - https://trello.com/b/xYRZCrgS/chytry-kurnik

## Obrázky

[//]: # (!["předběžná analýza projektu"]&#40;Doc/Pictures/AnalyzaProjektu_č2.jpg&#41;)
!["Základní podoba projektu"](doc/images/ProjectsAnalysis_FinalStateBeta10.jpg)

## Důležité odkazy

### Architektura mikroservis
- “Microservices are small, autonomous services that work together.”
- https://www.revolgy.com/cs/znalosti-zkusenosti/blog/vyzkousejte-mikroservisy
- https://medium.com/openwise-tech-blog/mikroservisy-kam-se-podivas-6d81f6fb1f66
- https://www.youtube.com/watch?v=lL_j7ilk7rc

### Messaging system - kafka
- https://www.youtube.com/watch?v=uvb00oaa3k8

### Jak nasetupovat SYMLINK na USB port ubuntu rpi5

- ve složce `/etc/udev/rules.d/` vyzvoříme soubor například `11-arduino.rules`
- číslo na začátku je důležité a nesmí být stejné s žádným rules souborem jinak ho systémové rules přemlasknou a nebude to fungovat
- do něj se v píší co řádek co symlink
- zadávají se parametry s názvy stejnými jak při výpisu příkazu `sudo udevadm info --name=/dev/ttyUSB1 --attribute-walk`
- na závěr se přidá samotný název symlinku SYMLINK+="arduinoSymlink"
- příklad pravidla:
- `# Arduino Scale 0`
- `SUBSYSTEM=="tty", KERNELS=="1-1.3", ATTRS{idVendor}=="1a86", ATTRS{idProduct}=="7523", SYMLINK+="arduinoScale0"`
- následně uložit soubor 
- znovu načtení a aktivace pravidel se provede příkazy
- `sudo udevadm control --reload-rules`
- a následně
- `sudo udevadm trigger`

