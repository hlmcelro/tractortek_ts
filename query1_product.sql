select ii.prod_code, 
	ii.product_name,
	sum(ps.sales_quantity) as total_qty_sold, ii.price, 
	ii.warranty_price,
	ps.sales_quantity * ii.price as total_product, 
	ps.sales_quantity * ii.warranty_price as total_warranty,
	(ps.sales_quantity * ii.price) + (ps.sales_quantity * ii.warranty_price) as total_sales
from product_sales ps cross join item_info ii
	on ii.prod_code = ps.item_code
group by prod_code;