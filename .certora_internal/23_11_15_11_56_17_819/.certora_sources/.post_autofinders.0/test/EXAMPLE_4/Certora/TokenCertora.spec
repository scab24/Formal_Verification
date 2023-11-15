methods {
  function mint(address user, uint256 amount) external;
  function transfer(address to, uint amount) external;
  function balanceOf(address) external returns (uint256) envfree;
}

rule mintIncreasesBalance(address user, uint256 amount) {
  env e;

  mathint originalBalance = balanceOf(e, user);

  mint(e, user, amount);

  assert balanceOf(e, user) == assert_uint256(originalBalance + amount),
         "Mint should increase balance";
}

rule transferDecreasesSenderBalance(address from, address to, uint amount) {
  env e;
  
  mathint fromBalanceBefore = balanceOf(e, from);

  transfer(e, to, amount);

  assert balanceOf(e, from) == assert_uint256(fromBalanceBefore - amount),
         "Transfer should decrease sender balance";  
}
rule transferIncreasesRecipientBalance(address from, address to, uint amount) {
  env e;

  mathint toBalanceBefore = balanceOf(e, to);

  transfer(e, to, amount);

  assert balanceOf(e, to) == assert_uint256(toBalanceBefore + amount),
         "Transfer should increase recipient balance";
}