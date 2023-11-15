methods {
    function backdoor(uint256 x) external pure;
}

rule checkBackdoor(uint256 x) {
    env e;

    backdoor(e, x);

}