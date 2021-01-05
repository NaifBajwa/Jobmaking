export interface Task {
    id?: string;
    title: string;
    description: string;
}

export interface Task1 {
    ID?: string;
    Name: string;
    Yrke: string;
    num: string;
    phone: string;
    email: string;
    iprogram: string;
    jobb : {
        id: string;
        Annonstitel: string;
        Arbetsgivare: string;
        Sistadatum: string;
        url: string;}[];
}
