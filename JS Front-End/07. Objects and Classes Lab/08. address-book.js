function addressBook(input) {
  let addressbook = {};
  for (let line of input) {
    let [name, address] = line.split(":");
    addressbook[name] = address;
  }

  let sortedAddressBookArr = Object.entries(addressbook).sort((a, b) =>
    a[0].localeCompare(b[0])
  );
  let sortedAddressBook = Object.fromEntries(sortedAddressBookArr);

  for (key in sortedAddressBook) {
    console.log(`${key} -> ${sortedAddressBook[key]}`);
  }
}

addressBook([
  "Tim:Doe Crossing",
  "Bill:Nelson Place",
  "Peter:Carlyle Ave",
  "Bill:Ornery Rd",
]);

addressBook([
  "Bob:Huxley Rd",
  "John:Milwaukee Crossing",
  "Peter:Fordem Ave",
  "Bob:Redwing Ave",
  "George:Mesta Crossing",
  "Ted:Gateway Way",
  "Bill:Gateway Way",
  "John:Grover Rd",
  "Peter:Huxley Rd",
  "Jeff:Gateway Way",
  "Jeff:Huxley Rd",
]);
