
CREATE TABLE `productos` (
  `id_producto` int(11) NOT NULL,
  `producto` varchar(400) NOT NULL,
  `descripcion` varchar(100) NOT NULL,
  `existencias` int(11) NOT NULL,
  `precio_compra` int(11) NOT NULL,
  `precio_venta` int(11) NOT NULL,
  `imagen_producto` varchar(100) CHARACTER SET utf8 COLLATE utf8_spanish_ci DEFAULT NULL,
  `posted_on` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `productos` (`id_producto`, `producto`, `descripcion`, `existencias`, `precio_compra`, `precio_venta`, `imagen_producto`, `posted_on`) VALUES
(3, 'Jabon', 'Caja', 25, 5000, 6200, NULL, '2017-03-23 14:46:06'),
(5, 'Champu', 'Paquete', 5, 1200, 1500, NULL, NULL);

