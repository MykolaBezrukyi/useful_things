db.irbLocationGroup.updateOne({"_id": ObjectId("63e25d17882cee6c71b6bdf3")}, {$addToSet: {"locations": "9971"}}); # add one value to a set
db.irbLocationGroup.updateOne({"_id": ObjectId("63e25d17882cee6c71b6bdf3")}, {$addToSet: {"locations": {$each: ["9971", "9973"]}}}); # add several values to a set
