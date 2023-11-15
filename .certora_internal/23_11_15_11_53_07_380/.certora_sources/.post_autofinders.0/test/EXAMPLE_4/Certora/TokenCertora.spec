methods {
  function mint(address user, uint256 amount) external;
  function transfer(address to, uint amount) external;
  function balanceOf(address user) external returns (uint256);
}

rule mintIncreasesBalance(address user, uint256 amount) {
  env e;

  address owner = e.msg.sender;

  uint256 originalBalance = balanceOf(user);

  mint(e, user, amount);

  assert balanceOf(user) == originalBalance + amount, 
         "Mint should increase balance";
}

rule transferDecreasesSenderBalance(address from, address to, uint amount) {
  env e;

  uint256 fromBalanceBefore = balanceOf(from);

  transfer(e, to, amount);

  assert balanceOf(from) == fromBalanceBefore - amount,
         "Transfer should decrease sender balance";
}

rule transferIncreasesRecipientBalance(address from, address to, uint amount) {
  env e;

  uint256 toBalanceBefore = balanceOf(to);

  transfer(e, to, amount);

  assert balanceOf(to) == toBalanceBefore + amount,
         "Transfer should increase recipient balance";
}