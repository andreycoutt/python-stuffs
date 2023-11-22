produtos = ["banana", "uva", "abacate"];
print(f"produtos: {type(produtos)}");
print(produtos);
produtos[0] = "melancia";
print(produtos);


lista_heterogenea = ["banana", 25, True, 10.99];
print(lista_heterogenea);
print(f"lista_heterogenea: {type(lista_heterogenea)}");


numeros_sorteados = {3, 5, 5, 11, 28, 55, 57};
print(numeros_sorteados);
print(f"numeros_sorteados: {type(numeros_sorteados)}");


produtos1 = {1: "banana", 2: "morango", 3: "uva", 4: "abacaxi", 5: "abacate"};
print(produtos1);
print(f"produtos1: {type(produtos1)}");


pessoa_1 = ("123.456.789-01", "Fulano de tal", True, 1800.00, 46);
print(pessoa_1);
print(f"pessoa_1: {type(pessoa_1)}");