age = 28

if age<18:
    print "just a teen"
elif age>=18 and age<25:
    print "enjoy it!"
else:
    print "sorry, the slope is downwards"

#Let's create a conditional for external Rvalue

season = "summer"

if season == "winter": #'==' means "is it equal to???" It's a question
    Rvalue = 0.03
    print "The Rvalue equals to "+str(Rvalue)
elif season == "summer":
    Rvalue = 0.44
    print "The Rvalue equals to "+str(Rvalue)
else:
    print "I don't know"
    
#Correct wide of wood stud

wide = 130

if wide == 90:
    Rvalue = 0.63
    
elif wide == 140:
    Rvalue = 0.98
   
else:
    Rvalue = ((0.63/90)*wide)    #If it would be 0.63*(wide/90), then we should convert wide to a float --> float (wide) so the division won't be zero.
print "The Rvalue equals to "+str(Rvalue)

Material_library = {"stucco_25mm":0.037,"faceBrick_100mm":0.075,"gypsumBoard_13mm":0.079,"wood_25mm":0.22,
"insideSurface":0.12,"outsideSurfaceSummer":0.044,"outsideSurfaceWinter":0.03}

Rvalue = Material_library ["stucco_25mm"]

print "The Rvalue of this material is "+str(Rvalue)

#Now we define the composition of a wall AS A LIST!!
layers_wall = ["faceBrick_100mm","wood_25mm"]

airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]

layers_wall_complete = layers_wall + airOnTwoSides #adding the two lists up, now we have all the layers of the wall for the heat transfer computation

#Now, to compute the Resistances, they can be calculated with the function "for"
for anyLayer in layers_wall_complete:
#print "this layer is: "+anyLayer
   RValue_layer = Material_library [anyLayer]
   print "this layer is: "+ anyLayer
   print "the value of R for this layer is: "+ str(RValue_layer)
   print "**************************"

#Now we compute the total Resistance
Rtot=0
for anyLayer in layers_wall_complete:
#print "this layer is: "+anyLayer
   RValue_layer = Material_library [anyLayer]
   Rtot=Rtot+RValue_layer
   print "this layer is: "+ anyLayer
   print "the value of R for this layer is: "+ str(RValue_layer)
   print "**************************"
print "the total R Value is "+str(Rtot)

#What if we would like to track all of the resistances' values
Rtot=0
RValues_layers = []
for anyLayer in layers_wall_complete:
#print "this layer is: "+anyLayer
   RValue_layer = Material_library [anyLayer]
   Rtot=Rtot+RValue_layer
   RValues_layers.append (RValue_layer)  #we use append to add every resistance value to the empty list we defined at the beggining
   print "this layer is: "+ anyLayer
   print "the value of R for this layer is: "+ str(RValue_layer)
   print "**************************"
print "the total R Value is "+str(Rtot)
   
#Step 1 of the Assignment: Do yesterday's exercise with dictionaries adding some other layers to the wall.

#Define lists of layers of an optional way
layers_wall_materials = ["faceBrick","wood"]
layers_wall_lengths = [100,13]
layers_wall = [{"material":"faceBrick", "length":100},{"material":"wood","length":13}]

Material_library = {"stucco":{"RValue":0.037,"length":13},"faceBrick":{"RValue":0.075,"length":100}

layers_wall = [{"material":"faceBrick","length":100},{"material":"wood","length":13}]


#functions Commmands!!!!!!!!!!!!!!!!!!!!!!

def powerOfN(x,n):
    """this function is clompetely useless, it just calculates x to the power of n""" #The description of the function that will appear when you'll try to use it 
    y = x**n    #Up to here, we defined our new function
    return y   #Output

result = powerOfN(2,5)     #it follows the order in which you defined the function
result = powerOfN(n=5,x=2) #you define the names, regardless of the order. YOU CANNOT MIX THIS TWO WAYS, YOU HAVE TO USE EITHER OF THE TWO.
result = powerOfN(n=10)

def sumPowersOf2 (x,y):
    """This function sums the powers of two variables x and y"""
    z=(x**2)+(y**2)
    return z
    
result = sumPowersOf2 (3,2)

#Step 2 of the Assignment: Do yesterday's exercise with FUNCTIONS adding some other layers to the wall.

def wall_calc (listOfLayers):
    Material_library = {"stucco_25mm":0.037,"faceBrick_100mm":0.075,"gypsumBoard_13mm":0.079,"wood_25mm":0.22,
        "insideSurface":0.12,"outsideSurfaceSummer":0.044,"outsideSurfaceWinter":0.03}
    airOnTwoSides = ["insideSurface","outsideSurfaceWinter"]
    layers_wall_complete = listOfLayers + airOnTwoSides
    Rtot=0
    RValues_layers=[]
    for anyLayer in layers_wall_complete:

        RValue_layer = Material_library [anyLayer]
        Rtot=Rtot+RValue_layer
        RValues_layers.append(RValue_layer)
        print "this layer is: "+ anyLayer
        print "the value of R for this layer is: "+ str(RValue_layer)
        print "**************************"
    print "the total R Value is "+str(Rtot)
    #return Rtot,RValue_layers
    #or
    results = {"Rtot":Rtot,"RValue of all layers":RValues_layers}
    return results
    
layers_wall = ["faceBrick_100mm","wood_25mm"]
results_ThisWall = wall_calc(layers_wall)

#For the assignment

def wall_calc (listOfLayersInSeries,ListOfParallelLayer,fraction):
    """here is the doc: this function receives two list of layers: in parallel and in series, and a fraction that is the ratio of the areas of the first layer in the layers in parallel""" 
#It's always winter