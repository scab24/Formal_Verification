methods {
    function mint(address user, uint256 amount) external;
    function transfer(address to, uint amount) external;
    function balanceOf(address user) external returns (uint256) envfree;
}

rule mintIncreasesBalance(address user, uint256 amount) {
    env e;

    assume e.msg.sender == owner; // Asegurar que el llamante es el dueño

    uint256 originalBalance = balanceOf(user);

    mint(e, user, amount);

    assert balanceOf(user) == originalBalance + amount,
           "Mint debe aumentar el balance del usuario en la cantidad especificada";
}

rule transferCorrectlyUpdatesBalances(address to, uint amount) {
    env e;

    uint256 senderOriginalBalance = balanceOf(e.msg.sender);
    uint256 recipientOriginalBalance = balanceOf(to);

    assume senderOriginalBalance >= amount; // Asegurar que el emisor tiene suficiente balance

    transfer(e, to, amount);

    assert balanceOf(e.msg.sender) == senderOriginalBalance - amount,
           "Transfer debe disminuir el balance del emisor en la cantidad especificada";

    assert balanceOf(to) == recipientOriginalBalance + amount,
           "Transfer debe aumentar el balance del receptor en la cantidad especificada";
}
