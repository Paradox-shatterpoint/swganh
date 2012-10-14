// This file is part of SWGANH which is released under the MIT license.
// See file LICENSE or go to http://swganh.com/LICENSE

#include "building.h"

using namespace std;
using namespace swganh::object;

uint32_t Building::GetType() const
{
    return type;
}

std::shared_ptr<Object> Building::Clone()
{
	boost::lock_guard<boost::mutex> lock(object_mutex_);
	auto other = make_shared<Building>();
	Clone(other);
	return other;
}

void Building::Clone(std::shared_ptr<Building> other)
{
	Tangible::Clone(other);
}