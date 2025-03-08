[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration)


# simple-clock-card
A text based simple clock for people who use Home Assistant on a panel

Based on https://github.com/arjhun/Homeassistant-Lovelace-Cards @arjhun


![24h clock](https://i.imgur.com/n37gyxZ.png)  

![military without seconds](https://i.imgur.com/ej4AFO3.png)

# Installation:
Follow only one of these installation methods.

<details>
  <summary><b>Installation and tracking with HACS:</b></summary>

1. You can install this custom component by adding this repository (https://github.com/fufar/simple-clock-card) to HACS in the settings menu of HACS first. You will find the custom component in the integration menu afterwards, look for 'Simple Clock Card'.

2. Set the lovelace panel
</details>

<details>
  <summary><b>Manual installation:</b></summary>

1. Copy nest-card2.js into your 'www' folder in the hass config directory. The *'www'* folder can be accesed via *'/local/'* in your configuration I've put my custom elements in the sub folder *'elements'* and the js file of this card in the folder *'simple-clock-card'* as an example.
2. Enable advanced mode and in your lovelace dashboard settings
3. Add a resource ![add a resource](https://i.imgur.com/pySUU4V.png)

   or if you use yaml to configure lovelace:

		resources:
			- type: module
	        	  url: /hacsfiles/elements/simple-clock-card/nest-card2.js
4. Set the lovelace panel
</details>


# Set lovelace panel

Add the following lines to a view in '*cards:*' as a *'manual card'* or use your yaml configuration and add:

		- type: 'custom:simple-clock-card'

## Options

| option             | default | description                                                                  |
|--------------------|:-------:|------------------------------------------------------------------------------|
| use_military       | true    | When true shows a 24h format clock instead of a 12h format clock with AM/ PM |
| hide_seconds       | false   | When true hides the seconds                                                  |
| bold_clock         | false   | When true makes the clock bold                                               |
| font_size          | 4rem    | Size of the font in rem. Units of measurement is required                    |
| lead_zero          | false   | When true adds a leading 0 to hours e.g. 04:28							      |
| paddingLeft_size   | 0px     | Size of the lovelace field in px. Units of measurement is required           |
| paddingRight_size  | 0px     | Size of the lovelace field in px. Units of measurement is required           |
| paddingTop_size    | 60px    | Size of the lovelace field in px. Units of measurement is required           |
| paddingBottom_size | 60px    | Size of the lovelace field in px. Units of measurement is required           |

## Example
- show a 24h clock with seconds:

		- type: 'custom:simple-clock-card'
		  use_military: true
		  hide_seconds: false
		  bold_clock: false
		  font_size: 6rem
		  paddingLeft_size: 32px
		  paddingRight_size: 32px
		  paddingTop_size: 32px
		  paddingBottom_size: 32px

Original author: github.com/arjhun



// set hass(hass) {
//
//     if (!this.content) {
//         var config = this.config;
//         const card = document.createElement('HA-card');
//         this.content = document.createElement('div');
//         this.content.style.paddingLeft = this.config.paddingLeft_size ? this.config.paddingLeft_size : '0px';
//         this.content.style.paddingRight = this.config.paddingRight_size ? this.config.paddingRight_size : '0px';
//         this.content.style.paddingTop = this.config.paddingTop_size ? this.config.paddingTop_size : '60px';
//         this.content.style.paddingBottom = this.config.paddingBottom_size ? this.config.paddingBottom_size : '60px';
//         this.content.style.fontSize = this.config.font_size ? this.config.font_size : '4rem';
//         this.content.style.fontWeight = this.config.bold_clock ? '900' : undefined;
//         this.style.textAlign = 'center';
//         this.content.style.display = 'inline-block';
//         card.appendChild(this.content);
//         this.appendChild(card);
//         var content = this.content;
//         startTime();
//         setInterval(startTime, 1000);
//
//         function addZero(i) {
//             if (i < 10) {
//                 i = "0" + i;
//             }
//             return i;
//         }
//
//         function startTime() {
//             var today = new Date(),
//                 h = today.getHours(),
//                 m = today.getMinutes(),
//                 s = today.getSeconds(),
//                 p = (h < 12) ? "AM" : "PM";
//             m = addZero(m);
//             s = addZero(s);
//
//             let use_military = config.use_military !== undefined ? config.use_military : true;
//             let hide_seconds = config.hide_seconds !== undefined ? config.hide_seconds : false;
//             let lead_zero = config.lead_zero !== undefined ? config.lead_zero : false;
//
//             let time_str = (use_military ? (lead_zero ? addZero(h) : h) : ((h + 11) % 12) + 1) +
//                 ":" +
//                 m +
//                 (hide_seconds ? "" : ":" + s) +
//                 (use_military ? " " : " " + p);
//             content.innerHTML = time_str;
//         }
//     }
// }
//
// setConfig(config) {
//     this.config = config;
// }
//
// getCardSize() {
//     return 1;
// }
