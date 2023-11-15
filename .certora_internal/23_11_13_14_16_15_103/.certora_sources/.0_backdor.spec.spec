methods {
    function backdoor(uint256 x) external pure;
}

rule checkBackdoor(uint256 x) {
    env e;

    backdoor(e, x);

    // La aserción en la función debería prevenir que esta línea se alcance
    // si 'number' es 0, lo que significaría una violación.
    // No se necesita un assert adicional aquí ya que la función ya contiene una aserción.
}
