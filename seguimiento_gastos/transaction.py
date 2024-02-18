class Transaction:
    """Representa una transacción financiera."""

    def __init__(self, amount, date, description, transaction_type):
        """Inicializa una nueva instancia de Transaction.

        Args:
            amount (float): El monto de la transacción.
            date (str): La fecha de la transacción en formato YYYY-MM-DD.
            description (str): La descripción de la transacción.
            transaction_type (str): El tipo de transacción (ingreso/gasto).
        """
        self.amount = amount
        self.date = date
        self.description = description
        self.transaction_type = transaction_type

    def __str__(self):
        """Devuelve una representación en cadena de la transacción."""
        return f"{self.date}: {self.description} ({self.amount} {self.transaction_type})"


