#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Creature()

	result.template = "object/mobile/vehicle/shared_landspeeder_av21.iff"
	result.attribute_template_id = 9
	result.stfName("monster_name","landspeeder_av21")		
	
	#### BEGIN MODIFICATIONS ####
	result.customization = '\x02\x11\xC3\x9D\x28\xC3\xBF\x01\xC3\x9E\xC3\x8D\xC3\xBF\x01\xC3\xA2\x1E\xC3\xBF\x01\xC3\x9B\x1D\xC3\xBF\x01\xC3\x98\x2D\xC3\xBF\x01\xC3\x9A\x63\xC3\xBF\x01\xC3\x99\x05\xC3\xBF\x01\xC3\xA1\x19\xC3\xBF\x01\xC3\xA0\x14\xC3\xBF\x01\xC3\x9F\x05\xC3\xBF\x01\xC3\x9C\x46\xC3\xBF\x01\xC3\x95\x19\xC3\xBF\x01\x01\x04\xC3\x96\x67\xC3\xBF\x01\x22\x11\xC3\x97\xC3\x9B\xC3\xBF\x01\x02\x11\xC3\xBF\x03'
	result.pvp_status = PVPSTATUS.PvPStatus_None
	result.options_mask = 4224
	result.setStringAttribute("radial_filename", "radials.vehicle")
	####  END MODIFICATIONS  ####
	
	return result