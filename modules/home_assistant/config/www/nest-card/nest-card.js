class NestCard extends HTMLElement {
    set hass(hass) {
        if (!this.content) {
            const card = document.createElement('ha-card');
            this.content = document.createElement('div');
            this.content.style.width = '100%';
            this.content.style.display = 'flex';
            this.content.style.justifyContent = 'center';
            this.content.style.alignItems = 'center';
            this.content.style.flexDirection = 'column';

            card.appendChild(this.content);
            this.appendChild(card);
        }

        const separator = ";";
        const logging = this.config.logging || false;

        const nests_in_row = this.config.nests_in_row || 0;
        const nests_in_column = this.config.nests_in_column || 0;

        const entity_nests_id = this.config.entity_nests;
        const entity_nests = hass.states[entity_nests_id];

        const entity_eggs_id = this.config.entity_eggs;
        const entity_eggs = hass.states[entity_eggs_id];

        let data_nests = entity_nests.state;
        let data_eggs = entity_eggs.state;

        if (logging) {
            console.log(nests_in_row);
            console.log(nests_in_column);
            console.log(entity_nests);
            console.log(entity_eggs);
            console.log(data_nests);
            console.log(data_eggs)
        }

        if ((!data_nests.includes('o') && !data_nests.includes('f')) || (data_nests.length > 1 && !data_nests.includes(separator))) {
            this.content.innerHTML = `Entity id: ${entity_nests_id} - Waiting for data or bad format...`;
            console.log("bad data Entity id:" + entity_nests_id)
        }
        if (!this.containsNumber(data_eggs) || this.containsLetters(data_eggs)) {
            this.content.innerHTML = `Entity id: ${entity_eggs_id} - Waiting for data or bad format...`;
            console.log("bad data Entity id:" + entity_eggs_id)
        } else {
            let states = data_nests.split(separator);
            let counts = data_eggs.split(separator);

            let container = document.createElement("div");
            container.id = "nest-container";
            for (let i = 0; i < nests_in_column; i++) {
                let row = document.createElement("div");
                row.style.display = "flex";
                for (let j = 0; j < nests_in_row; j++) {
                    let id = j + i * nests_in_row;

                    if (logging)
                        console.log("nest - " + id)

                    const nest = document.createElement('div');
                    nest.style.width = "100px";
                    nest.style.height = "100px";
                    nest.style.position = "relative";
                    nest.style.margin = "5px";

                    const img = document.createElement('img');
                    img.src = "/local/nest-card/res/nest.png";
                    img.alt = "Nest" + id;
                    nest.appendChild(img);

                    if (id < states.length) {
                        if (states[id] === "o") {
                            const chicken = document.createElement('img');
                            chicken.src = "/local/nest-card/res/chicken.png";
                            chicken.alt = "Nest" + id;
                            chicken.style.width = "100px";
                            chicken.style.height = "100px";
                            chicken.style.position = "absolute";
                            chicken.style.left = "0";
                            nest.appendChild(chicken);
                        }
                    }

                    if (id < counts.length && counts[id] !== "0") {
                        const count = document.createElement('div');
                        count.style.position = "absolute";
                        count.style.left = "-10px";
                        count.style.top = "72px";
                        count.style.color = "black";
                        count.style.width = "100%";
                        count.style.textAlign = "right";
                        count.style.fontSize = "20px";
                        count.style.fontWeight = "bold";
                        count.textContent = counts[id]
                        nest.appendChild(count);
                    }
                    row.appendChild(nest);
                }
                container.appendChild(row);
            }
            this.content.innerHTML = container.innerHTML;
        }
    }


    containsNumber(str) {
        return str.match(/\d+/) !== null;
    }

    containsLetters(str) {
        return str.match(/[a-zA-Z]/) !== null;
    }

    setConfig(config) {
        this.config = config;
    }

    getCardSize() {
        return 1;
    }
}

customElements
    .define(
        'nest-card'
        ,
        NestCard
    )
;
