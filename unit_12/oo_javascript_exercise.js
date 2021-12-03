
class Vehicle{
    constructor(make, model, year){
        this.make = make;
        this.model = model;
        this.year = year;

    }

    honk(){
        return "Beep."
    }

    toString(){
        return `This vehicle is a ${this.make} ${this.model} from ${this.year}`
    }
}

class Car extends Vehicle {
   
    constructor(){
        super()
        this.numWheels = 4;
       
    }
   
  
}

class Motorcycle extends Vehicle {
   
    constructor(){
        super()
        this.numWheels = 2;
       
    }
    revEngine(){
        return "VROOM!!!"
    }
  
}

class Garage{
    constructor(capacity){
      
        this.capacity = capacity;
        this.vehicles = []
    }

    add(vehicle){
        if(this.vehicles.length <= this.capacity){
           if(vehicle instanceof Vehicle){
                this.vehicles.push(vehicle)}
            else{
                return "Only Vehicles can be added!!"
            }
        }
        else{
                return "Capacity is full, sorry!"
        }
    }
}
