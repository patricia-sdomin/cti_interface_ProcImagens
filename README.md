# cti_interface_ProcImagens

Control software for processing of materials and devices by ultraviolet laser.

Interface para controle de movimentos: Newport XPS C8 Motion Controller Software desenvolvido durante projeto de mestrado na FEEC Unicamp com o título: 'Software de Controle para Sistema de Processamento de Materiais e Dispositivos por Laser Ultravioleta'. Em colaboração com o Centro de Pesquisa CTI Renato Archer - www.cti.gov.br na Divisão de Tecnologias Tridimensionais - DT3D.

Desenvolvido por Patrícia Silva Domingues.

**Versions**  
Python 2.7 (limitação pela biblioteca da controladora de movimentos/Newport)  with Tkinter GUI and Ttk module  
PIL -> 1.1.7  
Numpy -> 1.6.1  
Scipy -> 0.9.0  
Scikit-image->0.11.2  
Matplotlib -> 1.1.1rc0  

The system is formed by the following components:
- Host Computer - (with Linux or windows 7, which contains the Python Software) with dedicated Network Interface (10/100Base-T Ethernet) to connect through Motion Controller via a crossover cable. 
- Newport High Performance Motion Controller - Driver XPS - C8 (controladora de movimentos) with Real Time O.S. VxWorks 5.4.2; kernel 1.25; Web-Server version 2.5.2; stages database version 2.6.5.
- Pulseo - High Peak Power, Diode Pumped, Q-Switched, 355nm Laser System – Ultraviolet pulses - Laser head - (Laser ultravioleta pulsado) - Neodymium-doped yttrium orthovanadate (Vanadate Crystals) - Nd: YVO_4.
- Newport Spectra-Physics Power Supply model J200 (Fonte do laser).
- Elementos mecânicos de posicionamento e alinhamento.
- Componentes óticos específicos para o comprimento de onda do laser: três espelhos dielétricos com recobrimento antirrefletor e uma lente plano-convexa de ajuste focal.
- Newport High-Performance Long-Travel Linear Motor Stages - IMS400-LM (Posicionadores Lineares) – X and Y axes, with the following configurations: travel: 400mm; resolution: 0,02μm; maximum speed: 500mm/s.
- Newport Precision Vertical Stage – VP-5ZA (Posicionador Vertical) – Z axis, with the following configurations: travel: 4,8mm; resolution: 0,06μm; speed: 5mm/s. Positioner to perform the focal adjustment according to the thickness of the substrate.
- Newport Motorized Stepper - Linear Actuator – CMA-25CCCL (Atuador Linear), with the following configurations: travel: 25mm; resolution: 0,2μm; speed: 0.4mm/s. The actuator is used when it is necessary to accommodate parts with a thickness greater than Z axis offset. It vertically moves the focus lens arm to keep proper focal adjustment.
- PolyScience Recirculator Chiller (Recirculador ligado à fonte e ao laser head).
- Newport RP Reliance Sealed Hole Table Top (mesa com sistema de amortecimento pneumático).

Lab picture: 
![labpicture](https://user-images.githubusercontent.com/16061028/35770075-1e018a80-08fc-11e8-847d-281217b31fb4.png)

Schematic drawing
![draw](https://user-images.githubusercontent.com/16061028/35770450-ab2505f8-0902-11e8-9fa7-eb38336681bf.png)

Software integration
![int](https://user-images.githubusercontent.com/16061028/35770044-b707ef40-08fb-11e8-803b-2398ba505637.png)

"PC Host" <-> "Motion Controller" connection
![tcpipcon](https://user-images.githubusercontent.com/16061028/35769965-6a5053e6-08fa-11e8-9940-ecb0fbf3847b.png)


Sofware Overview: 
![integration2](https://user-images.githubusercontent.com/16061028/35770344-52ca9c94-0900-11e8-8561-0a180e922a44.png)


### Software Interface

*Image processing:

Image processing guide:

![guide_imgp](https://user-images.githubusercontent.com/16061028/35770393-7b0e5dca-0901-11e8-9bed-6e18d76a8a74.png)

- Label Image Regions: Segmentation-use .PNG file.
- Sobel Edge map: Image edge detection Filter.
- Skeletonization: Reduces binary objects to 1 pixel wide representations.
It's possible to See SubImages: after using 'Label Image Regions' and Choosing a number to See the segmentation part in Image File.

*Image Execution: for this guide is used :
Synchronization of the output pulses from the motion controller to trigger IN the ultraviolet laser.
Sequence to perform Synchronization:
- 'Read Image File' -> 'Create Displacement Windows' -> 
- Enable external commands in Laser interface: ""GEXT: 1"" -> Execute File

* GEXT: (at laser interface): this command enables or disables the use of the gate control on the analog port - on the power supply. "GEXT: 1" - use the signals on the analog inputs.


### Software Application

* Sensor Gas Electrodes:     
(a) Alumina (Al<sub>2</sub>O<sub>3</sub>) substrate with gold deposition: interdigitaded electrodes being drawn.   (b) Alumina substrate with platinum deposition: laser focusing in between the pieces for later division.
![exemple](https://user-images.githubusercontent.com/16061028/35770579-231f57a0-0905-11e8-8d57-f8512f6eef5d.png)

Sensor Gas Electrodes: 
![example2](https://user-images.githubusercontent.com/16061028/35770571-0dbbe05e-0905-11e8-85e5-f152b60381a7.png)

Electrode Scanning Electron Microscope image:
![example3](https://user-images.githubusercontent.com/16061028/35770641-357f8c5c-0906-11e8-8231-b262cff20024.png)

   
       
* PMMA (polymethylmethacrylate) mold for a PDMS (Polydimethylsiloxane) microfluidic device  
Surface map of a PMMA mold obtained by the laser swelling method: 
![exemple4](https://user-images.githubusercontent.com/16061028/35770688-ec32f6b4-0906-11e8-8faf-7f0312226c68.png)
