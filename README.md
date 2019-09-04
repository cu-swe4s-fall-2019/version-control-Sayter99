# version_control
Get familiar with version control basics

# Changes
* Deal with special cases to avoid exceptions
   1. `0/0` => return `NaN` (not a number)
   2. `positive number/0` => return `Inf` (infinity)
   3. `negative number/0` => return `-Inf`
