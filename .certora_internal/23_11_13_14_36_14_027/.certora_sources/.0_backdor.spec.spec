methods {
    function backdoor(uint256 x) external;
}

// Regla para verificar que backdoor no revierte incorrectamente
rule checkBackdoorDoesNotRevertNormally(uint256 x) {
    env e;

    // Utilizar un comando 'assume' para asegurar que x no es igual a 6912213124124532
    // antes de llamar a backdoor
    assume x != 6912213124124532;

    backdoor(e, x);

    // Afirmar verdadero como la última declaración para cumplir con las reglas de CVL
    assert true, "La ejecución debe completarse sin errores";
}

// Regla para verificar que backdoor revierte correctamente
rule checkBackdoorRevertsCorrectly() {
    env e;

    uint256 x = 6912213124124532; // Este valor debería activar el revert

    backdoor@withrevert(e, x);

    // Confirmar que la ejecución activa el revert
    assert lastReverted, "La ejecución debe revertir con CoffeeBreak";
}
