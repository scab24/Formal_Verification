methods {
    function mint(address user, uint256 amount) external;
    function transfer(address to, uint amount) external;
    function balanceOf(address user) external returns (uint256) envfree;
}

ghost address owner;

// Regla para verificar que solo el dueño puede acuñar tokens
rule onlyOwnerCanMint(address user, uint256 amount) {
    env e;
    require e.msg.sender != owner;

    mint@withrevert(e, user, amount);

    assert lastReverted, "La función mint debe revertir si el llamante no es el dueño";
}

// Regla para verificar que la función mint aumenta el balance correctamente
rule mintIncreasesBalance(address user, uint256 amount) {
    env e;
    require e.msg.sender == owner;

    mathint originalBalance = to_mathint(balanceOf(user));

    mint(e, user, amount);

    assert to_mathint(balanceOf(user)) == originalBalance + to_mathint(amount),
           "Mint debe aumentar el balance del usuario en la cantidad especificada";
}

// Regla para verificar que la función transfer actualiza los balances correctamente
rule transferCorrectlyUpdatesBalances(address from, address to, uint amount) {
    env e;

    require from != to;

    mathint senderOriginalBalance = to_mathint(balanceOf(from));
    mathint recipientOriginalBalance = to_mathint(balanceOf(to));

    require senderOriginalBalance >= to_mathint(amount);

    transfer(e, to, amount);

    assert to_mathint(balanceOf(from)) == senderOriginalBalance - to_mathint(amount),
           "Transfer debe disminuir el balance del emisor en la cantidad especificada";

    assert to_mathint(balanceOf(to)) == recipientOriginalBalance + to_mathint(amount),
           "Transfer debe aumentar el balance del receptor en la cantidad especificada";
}
