#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Tangible()

	result.template = "object/tangible/deed/pet_deed/shared_shear_mite_deed.iff"
	result.attribute_template_id = 2
	result.stfName("pet_deed","shear_mite")		
	
	#### BEGIN MODIFICATIONS ####
	result.setStringAttribute("radial_filename", "radials/deed_datapad.py")
	result.setStringAttribute("deed_result", "object/intangible/pet/shared_shear_mite_hue.iff")
	result.setStringAttribute("deed_mobile", "object/mobile/shared_shear_mite_hue.iff")
	####  END MODIFICATIONS  ####
	
	return result