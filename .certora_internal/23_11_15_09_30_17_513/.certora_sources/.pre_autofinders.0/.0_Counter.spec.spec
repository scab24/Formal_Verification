methods {
    function setNumber(uint256 newNumber, bool inLuck) external;
    function increment() external;
    function number() external returns (uint256) envfree;
}

/** @title setNumber establece number correctamente y revierte bajo ciertas condiciones */
rule setNumberBehavior(uint256 newNumber, bool inLuck) {
    env e;

    setNumber@withrevert(e, newNumber, inLuck);

    if (newNumber == 0xC0FFEE && inLuck) {
        assert lastReverted,
               "Must revert with CoffeeBreak if newNumber is 0xC0FFEE and inLuck is true";
    } else {
        assert number() == newNumber,
               "Number should be updated to newNumber if reversion conditions are not met";
    }
}

/** @title Increment aumenta number en uno */
rule incrementIncreasesNumber() {
    env e;

    mathint originalNumber = to_mathint(number());
    increment(e);
    mathint newNumber = to_mathint(number());

    assert newNumber == originalNumber + 1,
           "Increment should increase number by one";
}
