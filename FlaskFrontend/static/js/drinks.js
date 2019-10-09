function initNewDrink() {
    document.querySelector('.add-button').addEventListener('click', () =>
        App.util.toggle_child_visibility('.to-add'));

    document.querySelector('#form-drink').addEventListener('submit', (ev) => {
        ev.preventDefault();
        const drinkName = document.querySelector('#drink-name').value;
        if (drinkName.length < 1) alert('Drink name cannot be empty');
        else {
            App.req.post(location.href, {drinkName})
                .then(() => location.reload())
                .catch((err) => alert(err))
        }
    });

}

initNewDrink();