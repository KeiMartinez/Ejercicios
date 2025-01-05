export class FriendAge {
  constructor(name, year, month, day) {
      this.name = name;
      this.year = year;
      this.month = month;
      this.day = day;
  }

  returnAge() {
      const today = new Date();
      let age = today.getFullYear() - this.year;

      if (
          today.getMonth() < this.month - 1 ||
          (today.getMonth() === this.month - 1 && today.getDate() < this.day)
      ) {
          age--;
      }

      return `${this.name} is ${age} today!`;
  }
}
  