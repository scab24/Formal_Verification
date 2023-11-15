methods {
  function mint(address user, uint256 amount) external;
  function transfer(address to, uint amount) external;
  function balanceOf(address) external returns (uint256) envfree;
}

rule mintIncreasesBalance(address user, uint256 amount) {
  env e;
  
  address owner = e.msg.sender;

  uint256 originalBalance = balanceOf(user);

  mint(e, user, amount);

  assert balanceOf(user) == originalBalance + amount, 
         "Mint must increase balance";
}

rule transferCorrectlyUpdatesBalances(address from, address to, uint amount) {
  env e;

  require from != to;

  uint256 fromBalanceBefore = balanceOf(from);
  uint256 toBalanceBefore = balanceOf(to);

  require fromBalanceBefore >= amount;
  
  transfer(e, to, amount);

  assert balanceOf(from) == fromBalanceBefore - amount,
         "From balance must decrease";
         
  assert balanceOf(to) == toBalanceBefore + amount,
         "To balance must increase";  
}