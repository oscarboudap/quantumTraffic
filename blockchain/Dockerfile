FROM rust:latest
WORKDIR /blockchain
COPY . .
RUN cargo build --release
CMD ["./target/release/blockchain-node"]
