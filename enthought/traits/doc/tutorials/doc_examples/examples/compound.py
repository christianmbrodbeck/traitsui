#--[Imports]--------------------------------------------------------------------

from enthought.traits.api import Range, Trait

#--[Code]-----------------------------------------------------------------------

# Shows the definition of a compound trait.

class Die ( HasTraits ):
    
    # Define a compound trait definition:
    value = Trait( 1, Range( 1, 6 ), 
                  'one', 'two', 'three', 'four', 'five', 'six' )
                  
#--[Example*]-------------------------------------------------------------------

# Create a sample Die:
die = Die()

# Try out some sample valid values:
die.value = 3
die.value = 'three'
die.value = 5
die.value = 'five'

# Now try out some invalid values:

try:
    die.value = 0
except:
    import traceback
    traceback.print_exc()

try:
    die.value = 'zero'
except:
    import traceback
    traceback.print_exc()
    
