methods {
    function mint(address user, uint256 amount) external;
    function transfer(address to, uint amount) external;
    function balanceOf(address user) external returns (uint256) envfree;

}


// Rule to verify that the mint function increases the balance correctly
rule mintIncreasesBalance(address user, uint256 amount) {
    env e;
    require e.msg.sender == owner;

    mathint originalBalance = to_mathint(balanceOf(user));

    mint(e, user, amount);

    assert to_mathint(balanceOf(user)) == originalBalance + to_mathint(amount),
           "Mint must increase the user's balance by the specified amount";
}

// Rule to check that the transfer function updates the balances correctly
rule transferCorrectlyUpdatesBalances(address from, address to, uint amount) {
    env e;

    require from != to;

    mathint senderOriginalBalance = to_mathint(balanceOf(from));
    mathint recipientOriginalBalance = to_mathint(balanceOf(to));

    require senderOriginalBalance >= to_mathint(amount);

    transfer(e, to, amount);

    assert to_mathint(balanceOf(from)) == senderOriginalBalance - to_mathint(amount),
           "Transfer must decrease the balance sheet of the issuer by the specified amount";

    assert to_mathint(balanceOf(to)) == recipientOriginalBalance + to_mathint(amount),
           "Transfer must increase the balance of the receiver by the specified amount";
}
