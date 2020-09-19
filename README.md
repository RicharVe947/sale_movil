# sale_plan_service
Agrega funcionalidad de venta en prepago, plan y activación en ventas

#Estructura
Para el manejo de las ventas por 3 tipos se realizó lo siguiente:

    1.Se crean dos categorias en los productos (plan, Prepago) para que se den de alta los 
    productos y servicios pertenecientes a dichas categorias.

    2.Al momento de dar de alta un pedido de venta podemos seleccionar los productos
    estos pueden ser planes, prepago o ambos.
    
    3. Dentro del sale order line se encuentra la casilla activo que nos marcara si activaremos un producto
    en caso de ser asi nos pedira que seleccionemos una protección.

    De esta manera podemos tener los 3 casos o mas dentro de un mismo pedido de venta 