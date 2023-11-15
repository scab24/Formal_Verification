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

    assert to_mathint(totalAssets()) == to_mathint(originalTotalAssets + assets),
           "Total assets should increase by the deposited amount";

    assert to_mathint(totalShares()) == to_mathint(originalTotalShares + shares),
           "Total shares should increase by the calculated shares";

       // Verificar que la relación entre assets y shares es coherente
    assert totalShares() * originalTotalAssets == totalAssets() * originalTotalShares,
           "La relación entre totalAssets y totalShares debe mantenerse constante";
}

rule mintIncreasesAssetsAndShares(uint shares) {
    env e;

    uint originalTotalAssets = totalAssets();
    uint originalTotalShares = totalShares();

    uint assets = mint(e, shares);

    assert to_mathint(totalAssets()) == to_mathint(originalTotalAssets + assets),
           "Total assets should increase by the calculated assets";

    assert to_mathint(totalShares()) == to_mathint(originalTotalShares + shares),
           "Total shares should increase by the minted shares";

           // Verificar que la relación entre assets y shares es coherente
    assert totalShares() * originalTotalAssets == totalAssets() * originalTotalShares,
           "La relación entre totalAssets y totalShares debe mantenerse constante";
}
