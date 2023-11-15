methods {
    function backdoor(uint256 x) external ;
}

rule checkBackdoor(uint256 x) {
    env e;

    backdoor(e, x);

}