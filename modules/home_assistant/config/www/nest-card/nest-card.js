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

        const logging = this.config.logging || false;
        const nests_in_row = this.config.nests_in_row || 0;
        const nests_in_column = this.config.nests_in_column || 0;
        const separator = ";"
        const entityId = this.config.entity;
        const entity = hass.states[entityId];

        if (logging) {
            console.log(nests_in_row)
            console.log(nests_in_column);
            console.log(entity);
        }

        let data = entity.state
        if (logging)
            console.log(data)

        if ((!data.includes('o') && !data.includes('f')) || (data.length > 1 && !data.includes(separator))) {
            this.content.innerHTML = `Entity id: ${entityId} - Waiting for data...`;
        } else {
            let states = data.split(separator);

            let container = document.createElement("div");
            container.id = "nest-container";
            for (let i = 0; i < nests_in_column; i++) {
                let row = document.createElement("div");
                row.style.display = "flex";
                for (let j = 0; j < nests_in_row; j++) {
                    let id = j + i * nests_in_row;
                    console.log("nest - "+id)
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
                    row.appendChild(nest);
                }
                container.appendChild(row);
            }
            this.content.innerHTML = container.innerHTML;
        }
    }

    setConfig(config) {
        this.config = config;
    }

    getCardSize() {
        return 1;
    }
}

customElements.define('nest-card', NestCard);
