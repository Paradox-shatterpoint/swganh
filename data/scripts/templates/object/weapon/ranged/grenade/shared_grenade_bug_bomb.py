#### NOTICE: THIS FILE IS AUTOGENERATED
#### MODIFICATIONS MAY BE LOST IF DONE IMPROPERLY
#### PLEASE SEE THE ONLINE DOCUMENTATION FOR EXAMPLES

from swgpy.object import *	

def create(kernel):
	result = Weapon()

	result.template = "object/weapon/ranged/grenade/shared_grenade_bug_bomb.iff"
	result.attribute_template_id = 10
	result.stfName("weapon_name","grenade_bug_bomb")		
	
	#### BEGIN MODIFICATIONS ####
	####  END MODIFICATIONS  ####
	
	return result