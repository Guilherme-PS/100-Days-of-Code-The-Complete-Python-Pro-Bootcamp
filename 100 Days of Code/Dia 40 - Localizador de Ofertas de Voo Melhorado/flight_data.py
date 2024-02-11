class FlightData:

    def __init__(
        self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date,
            stop_overs=0, via_city=""):
        """
        Construtor da classe. Inicializa os atributos de preço, cidade e aeroporto de origem e destino,
        data de pertida e de retorno.
        :param price: Preço do voo.
        :param origin_city: Cidade de origem.
        :param origin_airport: Aeroporto de origem.
        :param destination_city: Cidade de destino.
        :param destination_airport: Aeroporto de destino.
        :param out_date: Data de partida.
        :param return_date: Data de retorno.
        :param stop_overs: Número de escalas
        :param via_city: Cidade de escalas
        """
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = stop_overs
        self.via_city = via_city
