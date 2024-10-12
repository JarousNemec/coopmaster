# CoopMaster
CoopMaster je chytrá aplikace pro správu kurníku, která automatizuje klíčové úkoly jako otevírání dveří a sledování zdraví slepic.
 Díky senzorům a kamerám zajišťuje bezpečnost a pohodlí slepic, zatímco farmář může kurník ovládat na dálku přes mobilní zařízení. Optimalizuje produkci a šetří čas díky automatizaci a monitoringu.

## Co je to Agilní vývoj
https://thinkeasy.cz/co-je-agilni-vyvoj-a-proc-ho-pouzivame/

## Postup řešení

### Backlog
  - vytvořit demo jednotlivých modulů
  - propojit moduly s Home Assistentem
  - udělat testy(test driven development)
  - dokončit moduly
  - dockerfile pro každou servisu
  - docker compose pro spuštění jednoho modulu
  - docker compose pro spuštění modulů, brokeru a Home Assistenta
  - github pipeline pro 
    - build docker imagů 
    - testy
  - fyzická instalace systému do kurníku
  - 
    
### 0. Sprint
 - analýza softwarového řešení 
 - v dalších sprintech proběhne postupná implementace

### 1. Sprint
 - vytvořit demo každého modulu(pouze core servisu s mock daty)
 - každá core servisa bude komunikovat přes mqtt broker 
 - mqtt credentials zatím v kodu

### 2. Sprint
 - docker compose pro současně spuštění demo modulů, brokeru a HA
 - credentials předělat do env v dockeru

### 3. Sprint 
 - přidat jednotlivé moduly do Home Assistenta

### 4. Sprint 
 - dodělat všechny subservisy modulů
 - napsat testy pro jednotlivé klíčové funkce modulů

### 5. Sprint
 - github pipeline pro build a testy

### 6. Sprint
 - dokončit moduly

### 7. Sprint
 - plně integrovat všechny moduly do Home Assistenta

### 9. Sprint
 - tuning neuronových sítí

### 10. Sprint
 - praktická implementace řešení v kurníku
 - řešení elektro instalace, připojení k internetu, nasazení softwaru na reálné železo



## Obrázky

[//]: # (!["předběžná analýza projektu"]&#40;Doc/Pictures/AnalyzaProjektu_č2.jpg&#41;)
!["Základní podoba projektu"](Doc/Pictures/ProjectsAnalysis_FinalStateBeta10.jpg)

## Důležité odkazy

### Architektura mikroservis
- “Microservices are small, autonomous services that work together.”
- https://www.revolgy.com/cs/znalosti-zkusenosti/blog/vyzkousejte-mikroservisy
- https://medium.com/openwise-tech-blog/mikroservisy-kam-se-podivas-6d81f6fb1f66
- https://www.youtube.com/watch?v=lL_j7ilk7rc

### Messaging system - kafka
- https://www.youtube.com/watch?v=uvb00oaa3k8 
