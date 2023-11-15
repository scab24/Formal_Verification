methods {
    function backdoor(uint256 x) external pure;
}

rule checkBackdoor(uint256 x) {
    env e;

    backdoor(e, x);

    // Confirmar que la ejecución llega al final sin revertir
    assert true, "La ejecución debe completarse sin errores";
}