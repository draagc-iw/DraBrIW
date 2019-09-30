const AppPages = {
  people: "#people-container",
  drinks: "#drinks-container"
};

function get_people() {
  const peopleReq = new XMLHttpRequest();
  const elementPersonList = document.querySelector('#people-list');
  const template = document.querySelector('#people-item');

  peopleReq.addEventListener('load', (e) => {
    const people = JSON.parse(peopleReq.response);
    people.forEach((person) => {
      const liElement = document.importNode(template.content, true);
      const elementName = liElement.querySelector('.people-item__first-name');
      const elementDrink = liElement.querySelector('.people-item__last-name');

      elementName.innerHTML = person['first_name'];
      elementDrink.innerHTML = person['last_name'];

      elementPersonList.appendChild(liElement);
    })
  });
  peopleReq.open('GET', 'http://10.0.1.72:8080/users');
  peopleReq.send()
}

function navigate(page){
  Object.values(AppPages).forEach((value) => document.querySelector(value).classList.add('hidden'));
  AppPages[page].classList.remove('hidden');
}

function init_menu() {
  document.querySelector(".vertical-menu").children.forEach((menuItem) => {
    menuItem.addEventListener('click', () => navigate(menuItem.att))
  });
  document.querySelector("#menu-item__people").addEventListener('click', () => navigate(AppPages.people));
  document.querySelector("#menu-item__people").addEventListener('click', () => na)
}

function init() {
  get_people();
  init_menu();
}

init();
