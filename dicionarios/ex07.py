dict_personal_data = {
    "nome" : "Luiz Marthus",
    "idade" : 19,
    "cpf" : "141.141.141-14",
    "cidade" : "Brasília",
    "telefone" : "+55 (61) 9 8191-9300"
}

dict_job_data = {
    "cargo" : "desempregado",
    "empresa" : "nenhuma",
    "salário" : 0,
    "tempo no cargo" : " 5 anos",
    "data de adesão" : "16-11-2020"
}

dict_entire_profile = dict_personal_data | dict_job_data

for k, v in dict_entire_profile.items():
    print(f"{k}   :   {v}")