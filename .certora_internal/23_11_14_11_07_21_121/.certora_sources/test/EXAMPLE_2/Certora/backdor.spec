methods {
    function backdoor(uint256 x) external;
}

/** @title Verify that backdoor does not revert for values of x other than 6912213124124532 */
rule backdoorDoesNotRevertNormally(uint256 x) {
    env e;

    // Ensure that x is not the value that triggers the reversion.
    require x != 6912213124124532;

    backdoor@withrevert(e, x);

    // Execution must complete without errors
    assert !lastReverted, "The function must not revert for values other than 6912213124124532.";
}

/** @title Verify that backdoor reverts to the value 6912213124124532 */
rule backdoorRevertsCorrectly() {
    env e;

    uint256 x = 6912213124124532; // This value should activate the revert

    backdoor@withrevert(e, x);

    assert lastReverted, "The execution must be reversed under specific conditions";
}
