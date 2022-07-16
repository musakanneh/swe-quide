const helpTheCashier = () => {
    let total = prompt('Total amount used: ');
    let moneytPaid = prompt('Tptal amount paid: ');
    total = parseFloat(total).toFixed(2);
    moneytPaid = parseFloat(moneytPaid).toFixed(2);

    let change  = (moneytPaid - total).toFixed(2);
    console.log(result = ('Due: £' + total + '/Paid: £' + moneytPaid + '/Change: £' + change));

    let noteCoins = [
        {
            value: 50,
            name: '£50 notes: '
        },
        {
            value: 20,
            name: '£20 notes: '
        },
        {
            value: 10,
            name: '£10 notes: '
        },
        {
            value: 5,
            name: '£50p coins: '
        },
        {
            value: 4,
            name: '£.40p coins: '
        },
        {
            value: 3,
            name: '£.30p coins: '
        },
        {
            value: 2,
            name: '£20p coins: '
        },
        {
            value: 1,
            name: '£10p coins: '
        }
    ];
    
    for (let i = 0; i < noteCoins.length; i++) {
        noteCoins[i].return = Math.floor(change / noteCoins[i].value);
        change = (change % noteCoins[i].value).toFixed(2);
        noteCoins[i].return > 0 ? (console.log(noteCoins[i].name + noteCoins[i].return)) : 0;
    }
};
console.log(helpTheCashier()); 