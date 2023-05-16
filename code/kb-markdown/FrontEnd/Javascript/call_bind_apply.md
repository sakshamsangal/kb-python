```


// call() used to invoke (call) a method with an owner object as an argument (parameter).



var person = {
  fullName: function() {
    return this.firstName + " " + this.lastName;
  }
};
var person1 = {
  firstName: "John",
  lastName: "Doe"
};
var person2 = {
  firstName: "Mary",
  lastName: "Doe"
};
person.fullName.call(person1); // Will return "John Doe"


var person = {
    fullName: function(city, country) {
      return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
  }
  var person1 = {
    firstName:"John",
    lastName: "Doe"
  }
  person.fullName.call(person1, "Oslo", "Norway");

// -------------------------------------------------------------
// apply method that can be used on different objects.
var person = {
    fullName: function() {
      return this.firstName + " " + this.lastName;
    }
  };
  var person1 = {
    firstName: "Mary",
    lastName: "Doe"
  };
  person.fullName.apply(person1); // Will return "Mary Doe"
  
  // The call() method takes arguments separately.
  // The apply() method takes arguments as an array.
  
  var person = {
    fullName: function(city, country) {
      return this.firstName + " " + this.lastName + "," + city + "," + country;
    }
  };
  var person1 = {
    firstName: "John",
    lastName: "Doe"
  };
  person.fullName.apply(person1, ["Oslo", "Norway"]);
  
// In JavaScript strict mode, if the first argument of the apply() method is not an object, it becomes the owner (object) of the invoked function. In "non-strict" mode, it becomes the global object.  

// Example showing binding some parameters
// bind() creates a new function 
var sum = function (a, b) {
  return a + b;
};

var add5 = sum.bind(null, 5);
console.log(add5(122));


//---------------------------
let celebrity = {
  "firstName": "shraddha",
  "lastname": "kapur"
}

function showAge(age) {
  console.log(this.firstName + " " + this.lastname + " age is " + age);
}

let person = {
  "firstName": "ram",
  "lastname": "pal"
}

// showAge.call(person, 24)
showAge.apply(person, [24])

let student = {
  "firstName": "pinky",
  "lastName": "agarwal"
}


let showStudent = showAge.bind(person, 12);
showStudent();


// problem
// 1. create multiple objects with fname, lname and fullName()
// 2. fullName() must not be repeated
// 3. create single code base for fullName()
// 4. every object must call fullName()

// solution
// 1. create person object with fname and lname
// 2. make fullName() separately 
// 3. apply call/apply/bind method to use fullName()

// call takes various argument 1 = pointer, 2 = argument, 3 = argument
// apply takes 2 argument 1 = pointer, 2 = array of arguments
// bind creates a copy of funtion 

let student = {
  "fname": "saksham",
  "lname": "sangal"
}

let teacher = {
  "fname": "sahitya",
  "lname": "kumar"
}

let fullName = function (age, state) {
  console.log(this.fname + " " + this.lname);
  console.log(age);
  console.log(state);
}

fullName.call(student, 23, "up");
fullName.apply(student, [23, "up"])
let myStudent = fullName.bind(student, 23, "up");
myStudent();

// ----

let student = {
  "fname": "saksham",
  "lname": "sangal"
}

let teacher = {
  "fname": "sahitya",
  "lname": "kumar"
}

let fullName = function () {
  console.log(this.fname + " " + this.lname);
}

Function.prototype.myBind = function(...args) {
  let obj = this;
  console.log(obj);
  
  return function () {
      obj.call(args[0]);
  }
}


let myStudent = fullName.myBind(student);
myStudent();  

var team = {
  participantOne: "Srishti",
  participantTwo: "Prateek",
  print: function () {
      /* TODO 1: 
      A. Define a function with identifier greetParticipants
      B. Pass the scope of the team object to greetParticipants function using bind() method
      C. The function greetParticipants must print the message to welcome both participants defined in the team object on the console, as shown in Problem Statement
      */
     var greetParticipants = function() {
          console.log('Welcome', this.participantOne, this.participantTwo);
     }.bind(this);
      greetParticipants();
  }
}
team.print();

```

```
var team = {
    participantOne: "Srishti",
    participantTwo: "Prateek",
    print: function () {
        /* TODO 1: 
        A. Define a function with identifier greetParticipants
        B. Pass the scope of the team object to greetParticipants function using bind() method
        C. The function greetParticipants must print the message to welcome both participants defined in the team object on the console, as shown in Problem Statement
        */
        var greetParticipants = function () {
            console.log("welcome" + " " + this.participantOne + " " + this.participantTwo);

        }.bind(this)
        greetParticipants();
    }
}
team.print();

var team = {
    participantOne: "Srishti",
    participantTwo: "Prateek",
    print: function () {
        /* TODO 2: 
        A. Define a function with identifier greetParticipants
        B. Pass the scope of the team object to greetParticipants function using call() method
        C. The function greetParticipants must print the message to welcome both participants defined in the team object on the console, as shown in Problem Statement
        */
        var greetParticipants = function () {
            console.log("welcome" + " " + this.participantOne + " " + this.participantTwo);

        }.call(this);
    }
}
team.print();

var team = {
    participants: ["Srishti", "Prateek"],
    print: function () {
        /* TODO 3: 
        A. Define a function with identifier greetParticipants
        B. Pass the scope of the team object to greetParticipants function using apply() method
        C. The function greetParticipants must print the message to welcome both participants defined in the team object on the console, as shown in Problem Statement
        */
        var greetParticipants = function (arr) {
            console.log("welcome" + " " + arr[0] + " " + arr[1]);

        }.apply(this, [this.participants]);
    }
}
team.print();
```