methods {
    function deposit(uint assets) external returns (uint);
    function mint(uint shares) external returns (uint);
    function totalAssets() external returns (uint) envfree;
    function totalShares() external returns (uint) envfree;
}

rule depositIncreasesAssetsAndShares(uint assets) {
    env e;

    uint originalTotalAssets = totalAssets();
    uint originalTotalShares = totalShares();

    uint shares = deposit(e, assets);

    assert totalAssets() == originalTotalAssets + assets,
           "Total assets should increase by the deposited amount";

    assert totalShares() == originalTotalShares + shares,
           "Total shares should increase by the calculated shares";
}

rule mintIncreasesAssetsAndShares(uint shares) {
    env e;

    uint originalTotalAssets = totalAssets();
    uint originalTotalShares = totalShares();

    uint assets = mint(e, shares);

    assert totalAssets() == originalTotalAssets + assets,
           "Total assets should increase by the calculated assets";

    assert totalShares() == originalTotalShares + shares,
           "Total shares should increase by the minted shares";
}
