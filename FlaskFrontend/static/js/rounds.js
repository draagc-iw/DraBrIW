function initNewRound() {
    const elAdd = document.querySelector('.list-add');
    if (elAdd) {
        elAdd.addEventListener('click', () =>
            App.util.toggle_child_visibility('.list-add'));

        elAdd.querySelectorAll('.to-add')
            .forEach((element) => element.addEventListener('click', () => {
                const path = '/app/rounds';
                const initiatorId = element.getAttribute('data-add-id');

                App.req.post(path, {id: initiatorId})
                    .then((response) => location.reload())
                    .catch((err) => alert(err));
            }));
    }

}

function initActiveSelector() {
    const activeRoundsBtn = document.querySelector('#btn-rnd-active');
    const allRoundsBtn = document.querySelector('#btn-rnd-all');
    activeRoundsBtn.addEventListener('click', () => {
        activeRoundsBtn.classList.add('active');
        allRoundsBtn.classList.remove('active');

        document.querySelectorAll('.block-list-item.closed')
            .forEach(element => element.classList.add('hidden'));
    });

    allRoundsBtn.addEventListener('click', () => {
        allRoundsBtn.classList.add('active');
        activeRoundsBtn.classList.remove('active');

        document.querySelectorAll('.block-list-item.closed')
            .forEach(element => element.classList.remove('hidden'));
    });
}

initActiveSelector();
initNewRound();
