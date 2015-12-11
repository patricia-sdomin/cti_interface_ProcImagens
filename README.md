# cti_interface_ProcImagens
Interface para controle de movimentos: Newport XPS C8 Motion Controller Software desenvolvido durante projeto de mestrado na FEEC Unicamp com o título: 'Software de Controle para Sistema de Processamento de Materiais e Dispositivos por Laser Ultravioleta'. Em colaboração com o Centro de Pesquisa CTI Renato Archer - www.cti.gov.br na Divisão de Tecnologias Tridimensionais - DT3D. 
Desenvolvido por Patrícia Silva Domingues.

**Versões usadas**
Python 2.7 (limitação pela biblioteca da controladora de movimentos/Newport)
PIL -> 1.1.7
Numpy -> 1.6.1
Scipy -> 0.9.0
Scikit-image->0.11.2
Matplotlib -> 1.1.1rc0


Software Interface: Newport XPS C8 Motion Controller with:

*Image processing:
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

 
@ISSUES: images

