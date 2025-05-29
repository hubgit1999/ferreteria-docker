CREATE SCHEMA ferreteria;

SET search_path TO ferreteria;

CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(20)
);

CREATE TABLE facturas (
    id_factura SERIAL PRIMARY KEY,
    fecha DATE DEFAULT CURRENT_DATE,
    id_cliente INT NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
);

CREATE TABLE categorias (
    id_categoria SERIAL PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL
);

CREATE TABLE proveedores (
    id_proveedor SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT,
    telefono VARCHAR(20)
);

CREATE TABLE productos (
    id_producto SERIAL PRIMARY KEY,
    descripcion TEXT NOT NULL,
    precio NUMERIC(10, 2) NOT NULL CHECK (precio >= 0),
    id_categoria INT NOT NULL,
    id_proveedor INT NOT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_proveedor) REFERENCES proveedores(id_proveedor)
);
