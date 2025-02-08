FROM rust:latest

WORKDIR /app

# Instalar dependencias adicionales
RUN apt-get update && apt-get install -y libssl-dev pkg-config

# Copiar el código fuente
COPY . .

# Compilar el código en modo release
RUN cargo build --release

CMD ["./target/release/blockchain_node"]
