function initNewPerson() {
    document.querySelector('.add-button').addEventListener('click', () =>
        App.util.toggle_child_visibility('.to-add'));

    document.querySelector('#form-person').addEventListener('submit', (ev) => {
        ev.preventDefault();
        const personFirstName = document.querySelector('#person-first-name').value;
        const personLastName = document.querySelector('#person-last-name').value;
        if (personFirstName.length < 1 || personLastName.length < 1) alert('Person name cannot be empty');
        else {
            App.req.post(location.href, {personFirstName, personLastName})
                .then(() => location.reload())
                .catch((err) => alert(err))
        }
    });

}

function initSelectFavDrink() {
    document.querySelectorAll('li.block-list-item')
        .forEach(personElement => {
                personElement.querySelectorAll('.edit, .close')
                    .forEach(bttn => bttn.addEventListener('click', () =>
                        App.util.toggle_child_visibility('li.block-list-item', personElement)));

                personElement.querySelectorAll('.to-add')
                    .forEach(drinkElement => drinkElement.addEventListener('click', () => {
                        const personId = drinkElement.getAttribute('data-person-id');
                        const drinkId = drinkElement.getAttribute('data-drink-id');

                        App.req.post(`/app/people/${personId}`, {drinkId})
                            .then(() => location.reload())
                            .catch((err) => alert(err));
                    }));
            }
        );

}

initNewPerson();
initSelectFavDrink();