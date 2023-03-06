function catCreator(arr) {
  class Cat {
    constructor(name, age) {
      this.name = name;
      this.age = age;
    }
    meow() {
      console.log(`${this.name}, age ${this.age} says Meow`);
    }
  }

  let cats = [];
  for (let i = 0; i < arr.length; i++) {
    let catData = arr[i].split(" ");
    cats.push(new Cat(catData[0], catData[1]));
  }

  for (let cat of cats) {
    cat.meow();
  }
}

catCreator(["Mellow 2", "Tom 5"]);
catCreator(["Candy 1", "Poppy 3", "Nyx 2"]);
