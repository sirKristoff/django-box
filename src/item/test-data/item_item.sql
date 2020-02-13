BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "item_item" (
	"id"	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	varchar(120) NOT NULL UNIQUE,
	"description"	text NOT NULL,
	"image"	varchar(100) NOT NULL
);

DELETE FROM "item_item";

INSERT INTO "item_item" ("id","name","description","image") VALUES
 (1,
  'Transil',
  'A **transient-voltage-suppression** (**TVS**) **diode**, also **transil** or **thyrector**, is an [electronic component][ElectronicComponent] used to protect [electronics][Electronics] from [voltage spikes][VoltageSpike] induced on connected wires.

[ElectronicComponent]: https://en.wikipedia.org/wiki/Electronic_component
[Electronics]: https://en.wikipedia.org/wiki/Electronics
[VoltageSpike]: https://en.wikipedia.org/wiki/Voltage_spike',
  'img/Transils.jpeg'),
 (2,
  'Transistor',
  'A **transistor** is a [semiconductor device][semiconductor device] used to [amplify][electronic amplifier] or [switch][switch] [electronic][electronic] signals and [electrical power][electrical power]. It is composed of [semiconductor][semiconductor] material usually with at least three [terminals][terminals] for connection to an external circuit. A [voltage][voltage] or [current][current] applied to one pair of the transistor''s terminals controls the current through another pair of terminals. Because the controlled (output) [power][power] can be higher than the controlling (input) power, a transistor can amplify a signal. Today, some transistors are packaged individually, but many more are found embedded in [integrated circuits][integrated circuits].

  [semiconductor device]: https://en.wikipedia.org/wiki/Semiconductor_device
  [electronic amplifier]: https://en.wikipedia.org/wiki/Electronic_amplifier
  [switch]: https://en.wikipedia.org/wiki/Switch "Switch"
  [electronic]: https://en.wikipedia.org/wiki/Electronics "Electronics"
  [electrical power]: https://en.wikipedia.org/wiki/Electrical_power "Electrical power"
  [semiconductor]: https://en.wikipedia.org/wiki/Semiconductor "Semiconductor"
  [terminals]: https://en.wikipedia.org/wiki/Terminal_(electronics) "Terminal (electronics)"
  [voltage]: https://en.wikipedia.org/wiki/Voltage "Voltage"
  [current]: https://en.wikipedia.org/wiki/Electric_current "Electric current"
  [power]: https://en.wikipedia.org/wiki/Electric_power "Electric power"
  [integrated circuits]: https://en.wikipedia.org/wiki/Integrated_circuit "Integrated circuit"

Austro-Hungarian [physicist][physicist] [Julius Edgar Lilienfeld][Julius Edgar Lilienfeld] proposed the concept of a [field-effect transistor][field-effect transistor] in 1926, but it was not possible to actually construct a working device at that time.[^1] The first working device to be built was a [point-contact transistor][point-contact transistor] invented in 1947 by American physicists [John Bardeen][John Bardeen] and Walter Brattain while working under [William Shockley][William Shockley] at [Bell Labs][Bell Labs]. They shared the 1956 [Nobel Prize in Physics][Nobel Prize in Physics] for their achievement. The most widely used transistor is the [MOSFET][MOSFET] (metal–oxide–semiconductor field-effect transistor), also known as the MOS transistor, which was invented by Egyptian engineer Mohamed Atalla with Korean engineer [Dawon Kahng][Dawon Kahng] at Bell Labs in 1959. The MOSFET was the first truly compact transistor that could be miniaturised and mass-produced for a wide range of uses.

  [physicist]: https://en.wikipedia.org/wiki/Physicist "Physicist"
  [Julius Edgar Lilienfeld]: https://en.wikipedia.org/wiki/Julius_Edgar_Lilienfeld "Julius Edgar Lilienfeld"
  [field-effect transistor]: https://en.wikipedia.org/wiki/Field-effect_transistor "Field-effect transistor"
  [point-contact transistor]: https://en.wikipedia.org/wiki/Point-contact_transistor "Point-contact transistor"
  [John Bardeen]: https://en.wikipedia.org/wiki/John_Bardeen "John Bardeen"
  [William Shockley]: https://en.wikipedia.org/wiki/William_Shockley "William Shockley"
  [Bell Labs]: https://en.wikipedia.org/wiki/Bell_Labs "Bell Labs"
  [Nobel Prize in Physics]: https://en.wikipedia.org/wiki/Nobel_Prize_in_Physics "Nobel Prize in Physics"
  [MOSFET]: https://en.wikipedia.org/wiki/MOSFET "MOSFET"
  [Dawon Kahng]: https://en.wikipedia.org/wiki/Dawon_Kahng "Dawon Kahng"
  
  [^1]: [1926 – Field Effect Semiconductor Device Concepts Patented](href="http://www.computerhistory.org/siliconengine/field-effect-semiconductor-device-concepts-patented/) *Computer History Museum*. [Archived](https://web.archive.org/web/20160322023120/http://www.computerhistory.org/siliconengine/field-effect-semiconductor-device-concepts-patented/) from the original on March 22, 2016. Retrieved March 25, 2016.',
  '../static/item/img/default_item_image.png'),
 (3,
  'Light-emitting diode',
  'A **light-emitting diode** (**LED** ![Alt](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/RBG-LED.jpg/320px-RBG-LED.jpg) is a [semiconductor][semiconductor] [light source][light source] that emits light when [current][current] flows through it. [Electrons][Electrons] in the semiconductor recombine with [electron holes][electron holes], releasing energy in the form of [photons][photons]. The color of the light (corresponding to the energy of the photons) is determined by the energy required for electrons to cross the [band gap][band gap] of the semiconductor. White light is obtained by using multiple semiconductors or a layer of light-emitting phosphor on the semiconductor device.

  [semiconductor]: https://en.wikipedia.org/wiki/Semiconductor "Semiconductor"
  [light source]: https://en.wikipedia.org/wiki/Light_source "Light source"
  [current]: https://en.wikipedia.org/wiki/Electric_current "Electric current"
  [Electrons]: https://en.wikipedia.org/wiki/Electron "Electron"
  [electron holes]: https://en.wikipedia.org/wiki/Electron_hole "Electron hole"
  [photons]: https://en.wikipedia.org/wiki/Photon "Photon"
  [band gap]: https://en.wikipedia.org/wiki/Band_gap "Band gap"',
  ''),
 (4,
  'Capacitor',
  'A **capacitor** is a device that stores [electrical energy] in an [electric field]. It is a [passive] [electronic component] with two [terminals].

The effect of a capacitor is known as [capacitance]. While some capacitance exists between any two electrical conductors in proximity in a [circuit], a capacitor is a component designed to add capacitance to a circuit. The capacitor was originally known as a **condenser** or **condensator**. This name and its cognates are still widely used in many languages, but rarely in English, one notable exception being [condenser microphones][condenser], also called capacitor microphones. 


## Theory of operation

### Overview

A capacitor consists of two [conductors][electrical conductor] separated by a non-conductive region.



  [capacitance]: https://en.wikipedia.org/wiki/Capacitance
  [circuit]: https://en.wikipedia.org/wiki/Electric_circuit
  [condenser]: https://en.wikipedia.org/wiki/Microphone#condenser
  [electric field]: https://en.wikipedia.org/wiki/Electric_field
  [electrical energy]: https://en.wikipedia.org/wiki/Electrical_energy
  [electrical conductor]: https://en.wikipedia.org/wiki/Electrical_conductor "Electrical conductor"
  [electronic component]: https://en.wikipedia.org/wiki/Electronic_component
  [passive]: https://en.wikipedia.org/wiki/Passivity_(engineering)
  [terminals]: https://en.wikipedia.org/wiki/Terminal_(electronics)',
  'img/Capacitor.jpg'),
 (5,
  'Some part',
  '## Description of part!

Hyper <a href="#">*link*</a>.',
  'img/item_feather-512.png');

COMMIT;
